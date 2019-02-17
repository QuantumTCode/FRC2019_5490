public List Turn(double x_object) '''Returns how much robot should turn'''{
    private static double perc_error = x_object/160 
    
    private Bool Positive_direction = True 
    if perc_error < 0 {
        Positive_direction = False
    }
    private static ret = new ArrayList(perc_error, Positive_direction)
    
    return ret
}