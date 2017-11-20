class Solution
    # @param a : constant array of integers
    # @return an integer
    def longestConsecutive(a)
        hash = {}
        min = a[0]
        max = a[0]
        a.each do |i|
            hash[i] = 1
            min = i < min ? i : min
            max = i > max ? i : max
        end
        
        cur_streak = 0
        max_streak = 0
        (min..max).to_a.each do |i|
            if (hash[i] != nil && hash[i] == 1)
                cur_streak = cur_streak + 1
                max_streak = cur_streak > max_streak && i == max ? cur_streak : max_streak
                else
                max_streak = cur_streak > max_streak ? cur_streak : max_streak
                cur_streak = 0
            end
        end
        
        return max_streak
    end
end