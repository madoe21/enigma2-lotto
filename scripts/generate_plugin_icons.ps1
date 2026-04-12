Add-Type -AssemblyName System.Drawing

$ErrorActionPreference = "Stop"

$baseDir = "c:\dev\enigma2\enigma2-lotto\src\LottoDE\res"
$targets = @(
    @{ Name = "plugin.png"; W = 256; H = 256 },
    @{ Name = "plugin_1x1.png"; W = 256; H = 256 },
    @{ Name = "plugin_16x9.png"; W = 320; H = 180 },
    @{ Name = "plugin_16x10.png"; W = 320; H = 200 },
    @{ Name = "plugin_4x3.png"; W = 320; H = 240 }
)

function New-Rect([double]$x, [double]$y, [double]$w, [double]$h) {
    return [System.Drawing.RectangleF]::new([single]$x, [single]$y, [single]$w, [single]$h)
}

function Draw-Ball {
    param(
        [System.Drawing.Graphics]$G,
        [double]$X,
        [double]$Y,
        [double]$Size,
        [string]$Text,
        [System.Drawing.Color]$ColorStart,
        [System.Drawing.Color]$ColorEnd
    )

    $rect = New-Rect $X $Y $Size $Size

    $gradient = [System.Drawing.Drawing2D.LinearGradientBrush]::new(
        $rect,
        $ColorStart,
        $ColorEnd,
        [System.Drawing.Drawing2D.LinearGradientMode]::ForwardDiagonal
    )
    $G.FillEllipse($gradient, $rect)
    $gradient.Dispose()

    $edgeWidth = [single][math]::Max(1.2, $Size * 0.045)
    $edgePen = [System.Drawing.Pen]::new([System.Drawing.Color]::FromArgb(225, 255, 255, 255), $edgeWidth)
    $G.DrawEllipse($edgePen, $rect)
    $edgePen.Dispose()

    $glossBrush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(105, 255, 255, 255))
    $glossRect = New-Rect ($X + $Size * 0.17) ($Y + $Size * 0.12) ($Size * 0.34) ($Size * 0.22)
    $G.FillEllipse($glossBrush, $glossRect)
    $glossBrush.Dispose()

    $fontSize = [single][math]::Max(8.0, $Size * 0.34)
    $font = [System.Drawing.Font]::new("Segoe UI", $fontSize, [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)
    $fmt = [System.Drawing.StringFormat]::new()
    $fmt.Alignment = [System.Drawing.StringAlignment]::Center
    $fmt.LineAlignment = [System.Drawing.StringAlignment]::Center

    $shadowRect = New-Rect ($X + 1) ($Y + 1) $Size $Size
    $shadowBrush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(130, 0, 0, 0))
    $textBrush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::White)

    $G.DrawString($Text, $font, $shadowBrush, $shadowRect, $fmt)
    $G.DrawString($Text, $font, $textBrush, $rect, $fmt)

    $shadowBrush.Dispose()
    $textBrush.Dispose()
    $font.Dispose()
    $fmt.Dispose()
}

function Make-Logo {
    param([string]$Path, [int]$W, [int]$H)

    $bmp = [System.Drawing.Bitmap]::new($W, $H, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    $g = [System.Drawing.Graphics]::FromImage($bmp)

    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
    $g.Clear([System.Drawing.Color]::Transparent)

    # Soft transparent glow to avoid hard empty corners but keep alpha background.
    $glowRect = New-Rect ($W * 0.03) ($H * 0.05) ($W * 0.94) ($H * 0.88)
    $glowBrush = [System.Drawing.Drawing2D.LinearGradientBrush]::new(
        $glowRect,
        [System.Drawing.Color]::FromArgb(70, 50, 140, 255),
        [System.Drawing.Color]::FromArgb(10, 20, 40, 80),
        [System.Drawing.Drawing2D.LinearGradientMode]::Vertical
    )
    $g.FillEllipse($glowBrush, $glowRect)
    $glowBrush.Dispose()

    $ballSize = [double][math]::Min($W, $H) * 0.255
    $startX = [double]$W * 0.012
    $topY = [double]$H * 0.03
    $step = ([double]$W - (2 * $startX) - $ballSize) / 5.0
    $nums = @("3", "11", "24", "36", "48", "49")

    for ($i = 0; $i -lt $nums.Length; $i++) {
        $x = $startX + ($step * $i)
        $y = $topY + ([math]::Sin($i * 1.1) * $ballSize * 0.10)
        Draw-Ball -G $g -X $x -Y $y -Size $ballSize -Text $nums[$i] -ColorStart ([System.Drawing.Color]::FromArgb(255, 255, 177, 67)) -ColorEnd ([System.Drawing.Color]::FromArgb(255, 224, 83, 22))
    }

    $superSize = $ballSize * 0.90
    Draw-Ball -G $g -X ($W * 0.78) -Y ($H * 0.38) -Size $superSize -Text "7" -ColorStart ([System.Drawing.Color]::FromArgb(255, 255, 86, 104)) -ColorEnd ([System.Drawing.Color]::FromArgb(255, 181, 13, 38))

    $plusFont = [System.Drawing.Font]::new("Segoe UI Black", [single][math]::Max(13.0, $H * 0.12), [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)
    $plusBrush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(245, 255, 255, 255))
    $g.DrawString("+", $plusFont, $plusBrush, [single]($W * 0.73), [single]($H * 0.44))
    $plusBrush.Dispose()
    $plusFont.Dispose()

    $titleFont = [System.Drawing.Font]::new("Segoe UI Black", [single][math]::Max(20.0, $H * 0.17), [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)
    $subFont = [System.Drawing.Font]::new("Segoe UI", [single][math]::Max(12.0, $H * 0.095), [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)

    $fmt = [System.Drawing.StringFormat]::new()
    $fmt.Alignment = [System.Drawing.StringAlignment]::Center
    $fmt.LineAlignment = [System.Drawing.StringAlignment]::Center

    $titleRect = New-Rect ($W * 0.01) ($H * 0.58) ($W * 0.98) ($H * 0.22)
    $subRect = New-Rect ($W * 0.01) ($H * 0.80) ($W * 0.98) ($H * 0.17)
    $titleShadowRect = New-Rect ($titleRect.X + 1) ($titleRect.Y + 1) $titleRect.Width $titleRect.Height
    $subShadowRect = New-Rect ($subRect.X + 1) ($subRect.Y + 1) $subRect.Width $subRect.Height

    $shadowBrush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(140, 0, 0, 0))
    $lottoBrush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(250, 255, 251, 216))
    $lineBrush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(250, 132, 231, 255))

    $g.DrawString("LOTTO", $titleFont, $shadowBrush, $titleShadowRect, $fmt)
    $g.DrawString("LOTTO", $titleFont, $lottoBrush, $titleRect, $fmt)
    $g.DrawString("6AUS49 | EUROJACKPOT", $subFont, $shadowBrush, $subShadowRect, $fmt)
    $g.DrawString("6AUS49 | EUROJACKPOT", $subFont, $lineBrush, $subRect, $fmt)

    $shadowBrush.Dispose()
    $lottoBrush.Dispose()
    $lineBrush.Dispose()
    $titleFont.Dispose()
    $subFont.Dispose()
    $fmt.Dispose()

    $bmp.Save($Path, [System.Drawing.Imaging.ImageFormat]::Png)
    $g.Dispose()
    $bmp.Dispose()
}

foreach ($t in $targets) {
    $outFile = Join-Path $baseDir $t.Name
    Make-Logo -Path $outFile -W $t.W -H $t.H
    Write-Output ("Wrote {0} ({1}x{2})" -f $t.Name, $t.W, $t.H)
}
