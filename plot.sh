#From Markus Seidel
# define custom colours
COLOR_RUN1="red!80!white"
COLOR_2016="blue!80!white"
COLOR_2016W="CadetBlue!40!white"
COLOR_RUN2="green!80!white"
# some useful style options for bands from https://gitlab.com/hepcedar/rivet/-/blob/release-3-1-x/doc/tutorials/makeplots.md
COMMON_TAGS="RatioPlotSameStyle=1:ErrorBars=0:ErrorBands=1:ErrorBandOpacity=0.25:PlotOrder=-1"
STYLE_RUN1="$COMMON_TAGS:ErrorBandColor=$COLOR_RUN1:LineColor=$COLOR_RUN1:PolyMarker=triangle*"
STYLE_2016="$COMMON_TAGS:ErrorBandColor=$COLOR_2016:LineColor=$COLOR_2016:PolyMarker=square*"
STYLE_2016W="$COMMON_TAGS:ErrorBandColor=$COLOR_2016W:LineColor=$COLOR_2016:PolyMarker=square*:ErrorBandStyle=vlines"
STYLE_RUN2="$COMMON_TAGS:ErrorBandColor=$COLOR_RUN2:LineColor=$COLOR_RUN2:PolyMarker=circle*:ErrorBandStyle=hlines"


rivet-mkhtml --errs -o /eos/user/e/efe/www/CMS_2015_I1384119_new \
    Run1.yoda:"Title=Run 1":$STYLE_RUN1 \
    CUETP8M2T4_13TeV_pythia8_unc.yoda:"Title=Early Run 2":$STYLE_2016 \
    CP5_13TeV_pythia8_unc.yoda:"Title=Run 2 Legacy":$STYLE_RUN2
