classdef Test_MSE < matlab.unittest.TestCase
    methods (Test)
        function testOutputMatrix(test)
            ref_mitrix = rand(5, 5);
            result_mitrix = rand(5, 5);
            expOut = sum((ref_mitrix(:)  -result_mitrix(:)) .^ 2) ...
                / numel(ref_mitrix);
            output = MSE_calculation(ref_mitrix, result_mitrix); 
            maxDiff = 10 ^ (-6);
            diff = abs(output - expOut);
            assertLessThanOrEqual(test, diff, maxDiff);
        end
    end
end
