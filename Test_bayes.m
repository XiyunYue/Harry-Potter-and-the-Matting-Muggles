classdef Test_bayes < matlab.unittest.TestCase
    methods (Test)
        function testOutputMatrix(testCase)
            in1 = 'image\G01\trimap.png';
            in2 = 'image\G01\input.png';
            p = makeParameters;
            [F, B, alpha_Ba] = bayes(in1, in2, p); 
            verifyTrue(testCase, all(alpha_Ba(:) == 0) & all(alpha_Ba(:) == 1));
        end
    end
end
