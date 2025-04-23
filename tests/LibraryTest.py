#!/usr/bin/env python3
import time
from mlstelemetry import MLSTelemetry


mlsClient = MLSTelemetry("mls_python_test", "Test1")

intValue = 100
floatValue = 132.55

#async counter
mlsClient.pushMetric(f'mls_python_asynccounter',"async_counter",intValue)
# counter
mlsClient.pushMetric(f'mls_python_counter',"counter",intValue)
# Gauge
mlsClient.pushMetric(f'mls_python_test_gauge',"gauge",floatValue)
# Log
mlsClient.pushLogInfo("MLSPythonTest Info Message",{"test": 2})

mlsClient.pushLogDebug("MLSPythonTest Debug Message",{"test": 2})
mlsClient.pushLogError("MLSPythonTest Error Message",{"test": 2})


time.sleep(2)