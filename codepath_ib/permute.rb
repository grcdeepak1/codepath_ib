class Solution
    # @param a : array of integers
    # @return an array of array of integers
    def permuteHelper(a, chosen, alreadyPrinted)
        #indent(chosen.length);
        #p "permuteHelper #{a}, #{chosen}"
        if (a.empty?)
            if (alreadyPrinted[chosen] != 1)
                #p chosen
                alreadyPrinted[chosen.clone] = 1
            end
        else
            # choose/explore/unchoose
            # (1 letter)
            a.each_index do |i|
                #choose
                c = a[i]
                chosen << c
                a.delete_at(i)
                
                #explore
                permuteHelper(a, chosen, alreadyPrinted)
                
                #un-choose
                a.insert(i, c)
                chosen.pop
            end
            
        end
        
        return
        
    end
    
    def permute(a)
        alreadyPrintedHash = {};
        permuteHelper(a, [], alreadyPrintedHash);
        return alreadyPrintedHash.keys;
    end
    
    def indent(n)
        n.times { print "    " }
    end
end

s = Solution.new
a = [1, 2, 3, 1];
p s.permute(a);