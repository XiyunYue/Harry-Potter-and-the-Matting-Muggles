classdef Test_combining < matlab.unittest.TestCase
    methods (Test)
        function testOutputMatrix(testCase)
            in1 = read_trimap('image\G01\trimap.png');
            in2 = double(imread('image\G01\background.png'));
            in3 = imread('image\G01\input.png');
            output = combining(in1, in2, in3); 
            verifySize(testCase, output, size(in3));
        end
    end
end
