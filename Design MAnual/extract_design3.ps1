$ErrorActionPreference = "Continue"
$base = (Resolve-Path "C:\Users\mrntau\OneDrive*N*\Skrivebord\Design MAnual\temp_pptx_extract\ppt\slides").Path
Write-Host "Resolved slides path: $base"

$allColors = @{}
$allFonts = @{}
$allSizes = @{}
$bgColors = @{}
$schemeColors = @{}
$alphaValues = @{}
$lineWidths = @{}
$boldSlides = @()
$italicSlides = @()
$spacingBefore = @{}
$spacingAfter = @{}
$marginLeft = @{}
$alignments = @{}

for ($i = 1; $i -le 13; $i++) {
    $file = Join-Path $base "slide$i.xml"
    if (-not (Test-Path $file)) {
        Write-Host "MISSING: $file"
        continue
    }
    $raw = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)
    Write-Host "Slide $i : $($raw.Length) chars"

    # srgb colors
    foreach ($m in [regex]::Matches($raw, 'srgbClr val="([A-Fa-f0-9]{6})"')) {
        $c = $m.Groups[1].Value
        if (-not $allColors.ContainsKey($c)) { $allColors[$c] = New-Object System.Collections.Generic.List[int] }
        if ($i -notin $allColors[$c]) { $allColors[$c].Add($i) }
    }

    # fonts (skip theme refs)
    foreach ($m in [regex]::Matches($raw, 'typeface="([^"]+)"')) {
        $f = $m.Groups[1].Value
        if ($f -match '^\+') { continue }
        if (-not $allFonts.ContainsKey($f)) { $allFonts[$f] = New-Object System.Collections.Generic.List[int] }
        if ($i -notin $allFonts[$f]) { $allFonts[$f].Add($i) }
    }

    # font sizes
    foreach ($m in [regex]::Matches($raw, ' sz="(\d+)"')) {
        $s = $m.Groups[1].Value
        if (-not $allSizes.ContainsKey($s)) { $allSizes[$s] = New-Object System.Collections.Generic.List[int] }
        if ($i -notin $allSizes[$s]) { $allSizes[$s].Add($i) }
    }

    # background
    foreach ($m in [regex]::Matches($raw, '<a:solidFill><a:srgbClr val="([A-Fa-f0-9]{6})"/></a:solidFill><a:effectLst/>')) {
        $c = $m.Groups[1].Value
        if (-not $bgColors.ContainsKey($c)) { $bgColors[$c] = New-Object System.Collections.Generic.List[int] }
        if ($i -notin $bgColors[$c]) { $bgColors[$c].Add($i) }
    }

    # scheme colors
    foreach ($m in [regex]::Matches($raw, 'schemeClr val="([^"]+)"')) {
        $sc = $m.Groups[1].Value
        if (-not $schemeColors.ContainsKey($sc)) { $schemeColors[$sc] = New-Object System.Collections.Generic.List[int] }
        if ($i -notin $schemeColors[$sc]) { $schemeColors[$sc].Add($i) }
    }

    # alpha
    foreach ($m in [regex]::Matches($raw, '<a:alpha val="(\d+)"')) {
        $a = $m.Groups[1].Value
        if (-not $alphaValues.ContainsKey($a)) { $alphaValues[$a] = New-Object System.Collections.Generic.List[int] }
        if ($i -notin $alphaValues[$a]) { $alphaValues[$a].Add($i) }
    }

    # line widths
    foreach ($m in [regex]::Matches($raw, '<a:ln w="(\d+)"')) {
        $w = $m.Groups[1].Value
        if (-not $lineWidths.ContainsKey($w)) { $lineWidths[$w] = New-Object System.Collections.Generic.List[int] }
        if ($i -notin $lineWidths[$w]) { $lineWidths[$w].Add($i) }
    }

    # bold
    if ($raw -match ' b="1"') { $boldSlides += $i }

    # italic
    if ($raw -match ' i="1"') { $italicSlides += $i }

    # alignments
    foreach ($m in [regex]::Matches($raw, 'algn="([^"]+)"')) {
        $al = $m.Groups[1].Value
        if (-not $alignments.ContainsKey($al)) { $alignments[$al] = New-Object System.Collections.Generic.List[int] }
        if ($i -notin $alignments[$al]) { $alignments[$al].Add($i) }
    }

    # margin left
    foreach ($m in [regex]::Matches($raw, 'marL="(\d+)"')) {
        $ml = $m.Groups[1].Value
        if (-not $marginLeft.ContainsKey($ml)) { $marginLeft[$ml] = New-Object System.Collections.Generic.List[int] }
        if ($i -notin $marginLeft[$ml]) { $marginLeft[$ml].Add($i) }
    }
}

Write-Host ""
Write-Host "=========================================="
Write-Host "  ALL SRGB COLORS (HEX)"
Write-Host "=========================================="
foreach ($c in ($allColors.Keys | Sort-Object)) {
    $slides = ($allColors[$c] | Sort-Object) -join ", "
    Write-Host "#$c  -> Slides: $slides"
}

Write-Host ""
Write-Host "=========================================="
Write-Host "  BACKGROUND COLORS"
Write-Host "=========================================="
foreach ($c in ($bgColors.Keys | Sort-Object)) {
    $slides = ($bgColors[$c] | Sort-Object) -join ", "
    Write-Host "#$c  -> Slides: $slides"
}

Write-Host ""
Write-Host "=========================================="
Write-Host "  EXPLICIT FONTS"
Write-Host "=========================================="
foreach ($f in ($allFonts.Keys | Sort-Object)) {
    $slides = ($allFonts[$f] | Sort-Object) -join ", "
    Write-Host "$f  -> Slides: $slides"
}

Write-Host ""
Write-Host "=========================================="
Write-Host "  FONT SIZES"
Write-Host "=========================================="
foreach ($s in ($allSizes.Keys | Sort-Object { [int]$_ })) {
    $pt = [int]$s / 100
    $slides = ($allSizes[$s] | Sort-Object) -join ", "
    Write-Host "${s} = ${pt}pt  -> Slides: $slides"
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
Write-Host "  ALPHA / TRANSPARENCY"
Write-Host "=========================================="
foreach ($a in ($alphaValues.Keys | Sort-Object)) {
    $slides = ($alphaValues[$a] | Sort-Object) -join ", "
    $pct = [int]$a / 1000
    Write-Host "${a} = ${pct}%  -> Slides: $slides"
}

Write-Host ""
Write-Host "=========================================="
Write-Host "  LINE WIDTHS"
Write-Host "=========================================="
foreach ($w in ($lineWidths.Keys | Sort-Object { [int]$_ })) {
    $pt = [math]::Round([int]$w / 12700, 2)
    $slides = ($lineWidths[$w] | Sort-Object) -join ", "
    Write-Host "${w} EMU = ${pt}pt  -> Slides: $slides"
}

Write-Host ""
Write-Host "=========================================="
Write-Host "  TEXT ALIGNMENT USAGE"
Write-Host "=========================================="
foreach ($al in ($alignments.Keys | Sort-Object)) {
    $slides = ($alignments[$al] | Sort-Object) -join ", "
    Write-Host "$al  -> Slides: $slides"
}

Write-Host ""
Write-Host "=========================================="
Write-Host "  MARGIN LEFT VALUES (EMU)"
Write-Host "=========================================="
foreach ($ml in ($marginLeft.Keys | Sort-Object { [int]$_ })) {
    $inches = [math]::Round([int]$ml / 914400, 2)
    $slides = ($marginLeft[$ml] | Sort-Object) -join ", "
    Write-Host "${ml} EMU = ${inches} in  -> Slides: $slides"
}

Write-Host ""
Write-Host "=========================================="
Write-Host "  BOLD / ITALIC"
Write-Host "=========================================="
Write-Host "Bold on slides: $($boldSlides -join ', ')"
Write-Host "Italic on slides: $($italicSlides -join ', ')"
