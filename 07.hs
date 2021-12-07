import Split (split)
import Data.List (sort)

f :: [Int] -> Int
f xs = foldr (\x -> (+ abs (median - x))) 0 xs
    where
        median :: Int
        median = (sort xs) !! ((1 + length xs) `div` 2)

g :: [Int] -> Int
g xs = minimum [calcFuel (mean-1), calcFuel (mean), calcFuel(mean+1) ]
    where
        mean :: Int
        mean = (sum xs) `div` (length xs)
        calcFuel :: Int -> Int
        calcFuel centre = sum $ map (\x -> sum [1..abs(centre - x)]) xs

main = do
    contents <- readFile "input/07.txt"
    let ss = lines contents
        xs :: [Int]
        xs = map read $ split "," $ head ss
    print ("#1: " ++ show (f xs))
    print ("#2: " ++ show (g xs))