import Split (split)

resetDayCount = 6
initialDayCount = 8

getInitialFishCount :: [Int] -> [Int]
getInitialFishCount xs = map (\x -> length $ filter (==x) xs) [0..initialDayCount]

countLanternFish :: Int -> [Int] -> Int
countLanternFish 0 xs    = sum xs
countLanternFish days xs = countLanternFish (days - 1) (map updateTimers [0..initialDayCount])
    where
        updateTimers :: Int -> Int
        updateTimers 6 = head xs + xs !! (resetDayCount+1)
        updateTimers 8 = head xs
        updateTimers x = xs !! (x+1)

f :: [Int] -> Int
f = countLanternFish 80 . getInitialFishCount

g :: [Int] -> Int
g = countLanternFish 256 . getInitialFishCount

main = do
    contents <- readFile "input/06.txt"
    let ss = lines contents
        xs :: [Int]
        xs = map read $ split "," $ head ss
    print ("#1: " ++ show (f xs))
    print ("#2: " ++ show (g xs))