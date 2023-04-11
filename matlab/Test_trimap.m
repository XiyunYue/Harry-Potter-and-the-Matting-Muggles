classdef Test_trimap < matlab.unittest.TestCase
    methods (Test)
        function testOutputMatrix(testCase)
            in = 'image\G01\trimap.png';
            output = read_trimap(in); 
            verifyTrue(testCase, all(output(:) >= 0) & all(output(:) <= 1));
        end
    end
end
