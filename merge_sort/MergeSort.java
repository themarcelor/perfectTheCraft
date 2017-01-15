import java.util.Arrays;

public class MergeSort {

    public static int[] arr = {19, 95, 15, 43, 27, 94, 17, 50,81, 2, 66};

    public static void merge(int[] arr, int[] temp, int leftStart, int leftEnd, int rightStart, int rightEnd) {
	int i = leftStart;
	int j = rightStart;
	int k = leftStart;

	while (i <= leftEnd && j <= rightEnd) {
	    if (arr[i] < arr[j]) {
		temp[k++] = arr[i++];
		System.out.println("_ temp_array - insert i: " + Arrays.toString(temp));
	    } else {
		temp[k++] = arr[j++];
		System.out.println("_ temp_array - insert j: " + Arrays.toString(temp));
	    }
	}
	while (i <= leftEnd) {
	    temp[k++] = arr[i++];
	    System.out.println("__ temp_array: " + Arrays.toString(temp));
	}
	while (j <= rightEnd) {
	    temp[k++] = arr[j++];
	    System.out.println("___ temp_array: " + Arrays.toString(temp));
	}
	for (i = leftStart; i <= rightEnd; i++) {
	    arr[i] = temp[i];
	}
	System.out.println(Arrays.toString(temp));
    }

    public static void mSort(int[] arr, int[] temp, int start, int end) {
	int splitPoint = (start + end)/2;
	System.out.println(splitPoint);

	if ((end - start) > 0) {
	    mSort(arr, temp, start, splitPoint);
	    mSort(arr, temp, splitPoint+1, end);
	    merge(arr, temp, start, splitPoint, splitPoint+1, end);
	}
    }

    public static void mergeSort(int[] arr) {
	int[] temp = new int[arr.length];
	mSort(arr, temp, 0, arr.length -1);
    }

    public static void main(String args[]) {
	mergeSort(arr);
	System.out.println(Arrays.toString(arr));
    }
}
