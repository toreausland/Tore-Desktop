$base = "C:\Users\mrntau\OneDrive - Mosseregionens Næringsutvikling AS\Skrivebord\Design MAnual\temp_pptx_extract\ppt\slides"

$allColors = @{}
$allFonts = @{}
$allSizes = @{}
$allBold = @{}
$allItalic = @{}
$bgColors = @{}
$schemeColors = @{}
$lineWidths = @{}
$alphaValues = @{}

for ($i = 1; $i -le 13; $i++) {
    $file = Join-Path $base "slide$i.xml"
    if (Test-Path $file) {
        $raw = Get-Content -Raw -Encoding UTF8 $file

        # Extract srgb colors
        $matches = [regex]::Matches($raw, 'srgbClr val="([A-Fa-f0-9]{6})"')
        foreach ($m in $matches) {
            $color = $m.Groups[1].Value
            if (-not $allColors.ContainsKey($color)) { $allColors[$color] = @() }
            if ($i -notin $allColors[$color]) { $allColors[$color] += $i }
        }

        # Extract fonts
        $matches = [regex]::Matches($raw, 'typeface="([^"]+)"')
        foreach ($m in $matches) {
            $font = $m.Groups[1].Value
            if ($font -notmatch '^\+') {  # Skip theme references like +mn-lt
                if (-not $allFonts.ContainsKey($font)) { $allFonts[$font] = @() }
                if ($i -notin $allFonts[$font]) { $allFonts[$font] += $i }
            }
        }

        # Extract font sizes
        $matches = [regex]::Matches($raw, ' sz="(\d+)"')
        foreach ($m in $matches) {
            $size = $m.Groups[1].Value
            if (-not $allSizes.ContainsKey($size)) { $allSizes[$size] = @() }
            if ($i -notin $allSizes[$size]) { $allSizes[$size] += $i }
        }

        # Extract background colors
        $matches = [regex]::Matches($raw, '<p:bg><p:bgPr><a:solidFill><a:srgbClr val="([A-Fa-f0-9]{6})"/>')
        foreach ($m in $matches) {
            $color = $m.Groups[1].Value
            if (-not $bgColors.ContainsKey($color)) { $bgColors[$color] = @() }
            if ($i -notin $bgColors[$color]) { $bgColors[$color] += $i }
        }

        # Extract scheme color references
        $matches = [regex]::Matches($raw, 'schemeClr val="([^"]+)"')
        foreach ($m in $matches) {
            $sc = $m.Groups[1].Value
            if (-not $schemeColors.ContainsKey($sc)) { $schemeColors[$sc] = @() }
            if ($i -notin $schemeColors[$sc]) { $schemeColors[$sc] += $i }
        }

        # Extract alpha values
        $matches = [regex]::Matches($raw, '<a:alpha val="(\d+)"')
        foreach ($m in $matches) {
            $alpha = $m.Groups[1].Value
            if (-not $alphaValues.ContainsKey($alpha)) { $alphaValues[$alpha] = @() }
            if ($i -notin $alphaValues[$alpha]) { $alphaValues[$alpha] += $i }
        }

        # Extract line widths
        $matches = [regex]::Matches($raw, '<a:ln w="(\d+)"')
        foreach ($m in $matches) {
            $w = $m.Groups[1].Value
            if (-not $lineWidths.ContainsKey($w)) { $lineWidths[$w] = @() }
            if ($i -notin $lineWidths[$w]) { $lineWidths[$w] += $i }
        }

        # Check bold/italic usage
        if ($raw -match ' b="1"') {
            if (-not $allBold.ContainsKey("bold")) { $allBold["bold"] = @() }
            if ($i -notin $allBold["bold"]) { $allBold["bold"] += $i }
        }
        if ($raw -match ' i="1"') {
            if (-not $allItalic.ContainsKey("italic")) { $allItalic["italic"] = @() }
            if ($i -notin $allItalic["italic"]) { $allItalic["italic"] += $i }
        }
    }
}

Write-Host "=========================================="
Write-Host "  ALL COLORS FOUND ACROSS ALL 13 SLIDES"
Write-Host "=========================================="
foreach ($color in ($allColors.Keys | Sort-Object)) {
    $slides = ($allColors[$color] | Sort-Object) -join ", "
    Write-Host "#$color  -> Slides: $slides"
}

Write-Host ""
Write-Host "=========================================="
Write-Host "  BACKGROUND COLORS"
Write-Host "=========================================="
foreach ($color in ($bgColors.Keys | Sort-Object)) {
    $slides = ($bgColors[$color] | Sort-Object) -join ", "
    Write-Host "#$color  -> Slides: $slides"
}

Write-Host ""
Write-Host "=========================================="
Write-Host "  ALL EXPLICIT FONTS"
Write-Host "=========================================="
foreach ($font in ($allFonts.Keys | Sort-Object)) {
    $slides = ($allFonts[$font] | Sort-Object) -join ", "
    Write-Host "$font  -> Slides: $slides"
}

Write-Host ""
Write-Host "=========================================="
Write-Host "  ALL FONT SIZES (in hundredths of pt)"
Write-Host "=========================================="
foreach ($size in ($allSizes.Keys | Sort-Object { [int]$_ })) {
    $ptSize = [int]$size / 100
    $slides = ($allSizes[$size] | Sort-Object) -join ", "
    Write-Host "${size} = ${ptSize}pt  -> Slides: $slides"
}

Write-Host ""
Write-Host "=========================================="
Write-Host "  SCHEME COLOR REFERENCES"
Write-Host "=========================================="
foreach ($sc in ($schemeColors.Keys | Sort-Object)) {
    $slides = ($schemeColors[$sc] | Sort-Object) -join ", "
    Write-Host "$sc  -> Slides: $slides"
}

Write-Host ""
Write-Host "=========================================="
Write-Host "  ALPHA (TRANSPARENCY) VALUES"
Write-Host "=========================================="
foreach ($a in ($alphaValues.Keys | Sort-Object)) {
    $slides = ($alphaValues[$a] | Sort-Object) -join ", "
    $pct = [int]$a / 1000
    Write-Host "${a} (${pct}%)  -> Slides: $slides"
}

Write-Host ""
Write-Host "=========================================="
Write-Host "  LINE WIDTHS (EMU)"
Write-Host "=========================================="
foreach ($w in ($lineWidths.Keys | Sort-Object { [int]$_ })) {
    $pt = [math]::Round([int]$w / 12700, 2)
    $slides = ($lineWidths[$w] | Sort-Object) -join ", "
    Write-Host "${w} EMU = ${pt}pt  -> Slides: $slides"
}

Write-Host ""
Write-Host "=========================================="
Write-Host "  BOLD / ITALIC USAGE"
Write-Host "=========================================="
if ($allBold.ContainsKey("bold")) {
    $slides = ($allBold["bold"] | Sort-Object) -join ", "
    Write-Host "Bold used on slides: $slides"
}
if ($allItalic.ContainsKey("italic")) {
    $slides = ($allItalic["italic"] | Sort-Object) -join ", "
    Write-Host "Italic used on slides: $slides"
}
