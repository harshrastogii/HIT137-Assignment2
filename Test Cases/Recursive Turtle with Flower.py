import turtle

def draw_tree(t, branch_len, left_angle, right_angle, reduction_factor, depth, is_first_branch=True):
    """
    Recursively draws a tree pattern with flowers at the tips.
    """
    if depth > 0:
        original_color = t.pencolor()
        original_size = t.pensize()
        
        if is_first_branch:
            t.color('brown')
            t.pensize(10)
        else:
            t.color('green')
            t.pensize(2)
            
        t.forward(branch_len)
        
        pos = t.position()
        heading = t.heading()
        
        # Adjust angles for middle branches to spread more
        adjusted_left_angle = left_angle + (5 * (depth - 1))
        adjusted_right_angle = right_angle + (5 * (depth - 1))
        
        # Draw right branch
        t.right(adjusted_right_angle)
        draw_tree(t, branch_len * reduction_factor, left_angle, right_angle, 
                 reduction_factor, depth - 1, False)
        
        t.penup()
        t.setposition(pos)
        t.setheading(heading)
        t.pendown()
        
        # Draw left branch
        t.left(adjusted_left_angle)
        draw_tree(t, branch_len * reduction_factor, left_angle, right_angle, 
                 reduction_factor, depth - 1, False)
        
        t.penup()
        t.setposition(pos)
        t.setheading(heading)
        t.pendown()
        
        t.color(original_color)
        t.pensize(original_size)
        t.backward(branch_len)
    else:
        # Draw a flower at the branch tip
        t.color('red')
        t.pensize(2)
        t.begin_fill()
        t.circle(5)
        t.end_fill()

def main():
    print("Enter the parameters for the fractal tree:")
    try:
        left_angle = float(input("Left branch angle (degrees): ")) + 20
        right_angle = float(input("Right branch angle (degrees): ")) + 20
        branch_len = float(input("Starting branch length (pixels): "))
        depth = int(input("Recursion depth: "))
        reduction = float(input("Branch length reduction factor (0-1): "))
        
        if reduction <= 0 or reduction >= 1:
            raise ValueError("Reduction factor must be between 0 and 1")
        if depth < 1:
            raise ValueError("Depth must be at least 1")
        if branch_len <= 0:
            raise ValueError("Branch length must be positive")
            
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    screen = turtle.Screen()
    screen.title("Fractal Tree with Flowers")
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    
    draw_tree(t, branch_len, left_angle, right_angle, reduction, depth, True)
    screen.exitonclick()

if __name__ == "__main__":
    main()