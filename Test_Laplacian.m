classdef Test_Laplacian < matlab.unittest.TestCase
    methods (Test)
        function testOutputMatrix(testCase)
            in1 = read_trimap('image\G01\trimap.png');
            in2 = imread('image\G01\input.png');
            output = Laplacian_matting(in1, in2); 
            verifyTrue(testCase, all(output(:) >= 0) & all(output(:) <= 1));
        end
    end
end
