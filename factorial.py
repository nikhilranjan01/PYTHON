n=int(input("enter no"))
ans=1
for i in range(1,n+1):
    ans=ans*i
print(ans)
'''
public class RaceSimulator {
    public static void main(String[] args) {
        int totalDistance = 50;  // Total distance from A to B (in km)
        int carPosition = 0;     // Car's initial position (in km)
        int bikePosition = 0;    // Bike's initial position (in km)
        int bikeFlatTirePosition = 30;  // Where the bike gets a flat tire (in km)
        int flatTireTime = 20 * 60;    // 20 minutes in seconds

        // Simulate the race
        for (int time = 0; carPosition < totalDistance && bikePosition < totalDistance; time++) {
            if (bikePosition < bikeFlatTirePosition) {
                bikePosition++;
            } else if (time < flatTireTime) {
             
            } else {
                bikePosition++;
            }
            
            carPosition++;

            System.out.println("Time: " + time + " seconds");
            System.out.println("Car's position: " + carPosition + " km");
            System.out.println("Bike's position: " + bikePosition + " km");
            System.out.println();

            if (carPosition >= totalDistance) {
                System.out.println("Car wins!");
            } else if (bikePosition >= totalDistance) {
                System.out.println("Bike wins!");
            }
        }
    }
}
'''