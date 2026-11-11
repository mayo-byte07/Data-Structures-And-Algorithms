class Solution {
    public long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        long totalCost = 0;

        if (cost1 + cost2 <= costBoth) {
            totalCost = 1L * cost1 * need1 + 1L * cost2 * need2;
        } else {
           
            int cnt_3 = Math.min(need1, need2);
            totalCost = 1L * cnt_3 * costBoth;

            need1 -= cnt_3;
            need2 -= cnt_3;
            if (need1 > 0) {
                totalCost += 1L * need1 * Math.min(cost1, costBoth);
                
            } else if (need2 > 0) {
                totalCost += 1L * need2 * Math.min(cost2, costBoth);
            }
        }

        return totalCost;
    }
}
