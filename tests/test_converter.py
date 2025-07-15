def test_basic_conversion(tmp_path):
    from gpx2csv.converter import gpx_to_csv
    test_gpx = 'examples/sba_to_temouchent.gpx'
    output_csv = tmp_path / 'output.csv'
    gpx_to_csv(test_gpx, output_csv)
    assert output_csv.exists()

