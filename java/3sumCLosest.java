int threeSumClosest(int[] numbers, int target) {
        
        Arrays.sort(numbers);
        
        int diff=Integer.MAX_VALUE;
        int closest=Integer.MAX_VALUE;
        
        for(int k=0;k<numbers.length-2;k++){
        
        int left=k+1;
        int right=numbers.length-1;
        
        while(left<right){
            
            int sum=numbers[k]+numbers[left]+numbers[right];
            
            if(Math.abs(sum-target)<diff){
                diff=Math.abs(sum-target);
                closest=sum;
            }
            
            if(sum==target){

                return sum;
            }
            
            else if(sum<target){
                
                left+=1;
            }
            
            else if(sum>target){
                right-=1;
            }
            
        }
        }
        
        return closest;
    }