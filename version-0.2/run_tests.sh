#!bash
echo "++++++++++++++++"
echo "TEST FFG:"
echo "++++++++++++++++"
python3 -m unittest -v tests/matter_setupFFGNuc_tests.py
#
echo "++++++++++++++++"
echo "TEST micro:"
echo "++++++++++++++++"
python3 -m unittest -v tests/matter_setupMicro_tests.py
#
echo "++++++++++++++++"
echo "TEST pheno:"
echo "++++++++++++++++"
#python3 -m unittest -v tests/setup_pheno_tests.py
#
echo "++++++++++++++++"
echo "TEST corr:"
echo "++++++++++++++++"
python3 -m unittest -v tests/corr_setupKsatQsat_tests.py
#
echo "++++++++++++++++"
echo "TEST astro:"
echo "++++++++++++++++"
python3 -m unittest -v tests/astro_setupMasses_tests.py
