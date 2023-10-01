from interpolation import lerp

class MovementHandler:
    def __init__(self, move_speed):
        self.move_speed = move_speed

    def move_towards(self, x, y, target_x, target_y):
        dx = target_x - x
        dy = target_y - y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance != 0:
            normalized_dx = dx / distance
            normalized_dy = dy / distance

            # Scale speed based on distance to cursor
            half_screen_distance = 400  # Replace with actual value
            speed_scale = min(distance / half_screen_distance, 1)
            scaled_speed = self.move_speed * speed_scale

            new_x = x + scaled_speed * normalized_dx
            new_y = y + scaled_speed * normalized_dy

            return new_x, new_y

