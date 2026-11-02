This project aims to simulate a particles motion within a tokamak magnetic field.
First I simulated using the Euler method, which added a growth factor to the gyroradius of √(1 + (ω·dt)². Regardless of the time step, the particle spirals out of the scope of the tokamak.
Next I did the same, with a Boris pushing method, which conserves energy and prevents unrealistic behavior. 
Then I worked on ways to compare the two methods, such as by plotting the distances between the two simulated particles over time.