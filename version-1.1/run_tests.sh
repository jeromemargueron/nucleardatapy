#!bash
echo "++++++++++++++++"
echo "TEST FFG:"
echo "++++++++++++++++"
python3 -m unittest -v tests/test_matter_setupFFGNuc.py
#
echo "++++++++++++++++"
echo "TEST micro:"
echo "++++++++++++++++"
python3 -m unittest -v tests/test_matter_setupMicro.py
#
echo "++++++++++++++++"
echo "TEST pheno:"
echo "++++++++++++++++"
#python3 -m unittest -v tests/test_setup_pheno.py
#
echo "++++++++++++++++"
echo "TEST corr:"
echo "++++++++++++++++"
python3 -m unittest -v tests/test_corr_setupKsatQsat.py
#
echo "++++++++++++++++"
echo "TEST astro:"
echo "++++++++++++++++"
python3 -m unittest -v tests/test_astro_setupMasses.py
