Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import numpy as np
import matplotlib.pyplot as plt
import math

# Constants
G = 9.81  # Acceleration due to gravity (m/s^2)
DT = 0.01 # Time step for numerical integration (s)

def simulate_projectile(initial_velocity, launch_angle_deg, mass=1.0):
    """
    Simulates 2D projectile motion under constant gravity.

    Args:
        initial_velocity (float): Initial speed (m/s).
        launch_angle_deg (float): Launch angle (degrees from horizontal).
        mass (float): Mass of the object (kg). (Used to demonstrate modularity, but not in current calculation)

    Returns:
        tuple: (x_positions, y_positions)
    """
    print(f"\n--- Running Projectile Simulation (v0={initial_velocity} m/s, angle={launch_angle_deg} deg) ---")

    # Convert angle to radians
    angle_rad = np.deg2rad(launch_angle_deg)

    # Initial velocities
    vx = initial_velocity * np.cos(angle_rad)
    vy = initial_velocity * np.sin(angle_rad)

    # Initial position
    x, y = 0.0, 0.0

    x_positions = [x]
    y_positions = [y]

    # Simulation loop
    time = 0.0
    while y >= 0 or time == 0:
        # Update velocity (Euler method)
        # Horizontal acceleration is zero (neglecting air resistance)
        # Vertical acceleration is -G
        vy -= G * DT

        # Update position
        x += vx * DT
        y += vy * DT

        x_positions.append(x)
        y_positions.append(y)

...         time += DT
...         if time > 100: # Safety break
...              break
... 
...     print(f"Simulation finished in {time:.2f} seconds.")
...     print(f"Max distance (Range): {x_positions[-1]:.2f} meters.")
...     print(f"Max height: {np.max(y_positions):.2f} meters.")
... 
...     return np.array(x_positions), np.array(y_positions)
... 
... def visualize_projectile(x_pos, y_pos):
...     """Plots the projectile trajectory."""
...     plt.figure(figsize=(10, 6))
...     plt.plot(x_pos, y_pos, label='Projectile Trajectory', color='#4CAF50', linewidth=2)
...     plt.title('Projectile Motion Simulation', fontsize=16)
...     plt.xlabel('Horizontal Distance (meters)', fontsize=12)
...     plt.ylabel('Vertical Height (meters)', fontsize=12)
...     plt.axhline(0, color='gray', linestyle='--', linewidth=0.5) # Ground line
...     plt.grid(True, linestyle=':', alpha=0.7)
...     plt.legend()
...     plt.axis('equal') # Keep scale consistent
...     plt.show()
... 
... def simulate_pendulum(length, initial_angle_deg, duration=10.0):
...     """
...     Simulates the motion of a simple pendulum using the Euler method.
... 
...     Args:
...         length (float): Length of the pendulum string (meters).
...         initial_angle_deg (float): Initial angle (degrees from vertical).
...         duration (float): Total simulation time (seconds).
... 
...     Returns:
...         tuple: (time_points, angle_points)
...     """
...     print(f"\n--- Running Pendulum Simulation (L={length} m, Angle={initial_angle_deg} deg) ---")
... 
...     # Convert initial angle to radians
    angle = np.deg2rad(initial_angle_deg)
    angular_velocity = 0.0
    time = 0.0

    time_points = [time]
    angle_points = [angle]

    # Simulation loop
    while time < duration:
        # Angular acceleration (alpha) is proportional to -sin(theta)
        # alpha = - (G / L) * sin(theta)
        angular_acceleration = - (G / length) * np.sin(angle)

        # Update angular velocity (Euler method)
        angular_velocity += angular_acceleration * DT

        # Update angle (Euler method)
        angle += angular_velocity * DT

        time += DT

        time_points.append(time)
        angle_points.append(angle)

    return np.array(time_points), np.array(angle_points)

def visualize_pendulum(time_points, angle_points):
    """Plots the angle over time for the pendulum."""
    plt.figure(figsize=(10, 6))

    # Convert angle back to degrees for clearer visualization
    angle_deg = np.rad2deg(angle_points)

    plt.plot(time_points, angle_deg, label='Angle over Time', color='#FF9800', linewidth=2)
    plt.title('Simple Pendulum Oscillation', fontsize=16)
    plt.xlabel('Time (seconds)', fontsize=12)
    plt.ylabel('Angle (degrees)', fontsize=12)
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.5) # Equilibrium line
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend()
    plt.show()

def main():
    """Runs the main physics simulations."""

    # 1. PROJECTILE MOTION EXAMPLE
    x_proj, y_proj = simulate_projectile(
        initial_velocity=40.0,   # 40 m/s
        launch_angle_deg=45.0    # 45 degrees
    )
    visualize_projectile(x_proj, y_proj)

    # 2. PENDULUM MOTION EXAMPLE
    t_pend, theta_pend = simulate_pendulum(
        length=2.0,              # 2.0 meters
        initial_angle_deg=30.0,  # 30 degrees
        duration=20.0            # Simulate for 20 seconds
    )
    visualize_pendulum(t_pend, theta_pend)

if __name__ == "__main__":
    main()
