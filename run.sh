pytest  -v  --junitxml=./TestReports/report_US.xml
sleep 3
pytest  -v  --locale IN --junitxml=./TestReports/report_IN.xml
