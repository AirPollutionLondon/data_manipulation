# Main directory
MDIR=$HOME/AirPollutionLondon/data_manipulation

# Script directory
SCDIR=$MDIR/data_generation

# Directory to output to
OUTDIR=$SCDIR/csvs

echo "Making output directory."
mkdir -p $OUTDIR

echo "Running Python scripts."

echo "Making user data"
python $SCDIR/user_data_generator.py "$OUTDIR/user_data.csv" -c 1000

echo "Making sensor metadata"
python $SCDIR/sensor_metadata_generator.py "$OUTDIR/sensor_metadata.csv" -c 10000

echo "Linking sensor metadata with user data"
python $SCDIR/data_metamodifier.py "$OUTDIR/sensor_metadata.csv" "$OUTDIR/user_data.csv" -o False

echo "Generating sensor readings"
python $SCDIR/sensor_reading_generator.py "$OUTDIR/sensor_readings.csv" "$OUTDIR/sensor_metadata.csv" -c 50000

echo "Done!"