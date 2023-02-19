public class Cell implements Comparable<Cell> {

    private int ID;
    private int priority;
    private int[] invalidNums;
    private boolean isFixed;
    private boolean inPlay;

    public Cell(int ID) {
        this.ID = ID;
        this.priority = 0;
        this.isFixed = false;
        this.inPlay = false;
        this.invalidNums = new int[9];
    }

    public void addInvalid(int val) {
        if (invalidNums[val - 1] == 0) {
            priority++;
        }
        invalidNums[val - 1]++;
    }

    public void removeInvalid(int val) {
        invalidNums[val - 1]--;
        if (invalidNums[val - 1] == 0) {
            priority--;
        }
    }

    public int getPriority() {
        return priority;
    }

    public void setPriority(int val) {
        this.priority = val;
    }

    public void setFixed() {
        this.isFixed = true;
    }

    public boolean isFixed() {
        return isFixed;
    }

    public void changeStatus(boolean stat) {
        this.inPlay = stat;
    }

    public boolean isInPlay() {
        return inPlay;
    }

    public int getID() {
        return ID;
    }

    public int[] getNotInvalid() {
        int[] arr = new int[9 - priority];
        int count = 0;
        for (int i = 0; i < invalidNums.length; i++) {
            if (invalidNums[i] == 0) {
                arr[count] = i + 1;
                count++;
            }
        }
        return arr;
    }

    public int compareTo(Cell other) {
        if (this.priority == other.priority) {
            return 0;
        } else if (this.priority < other.priority) {
            return -1;
        } else {
            return 1;
        }
    }

    public String toString() {
        return "(" + "[" + ID / 9 + "," + ID % 9 + "]" + "," + priority + ")";
    }

}