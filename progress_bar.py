import sys

def progress_bar(iteration, total, longitud=50):
    """
    Display a progress bar in the console.
    
    Args:
        iteration (int): Current iteration number
        total (int): Total number of iterations
        longitud (int): Length of the progress bar in characters (default: 50)
    """
    # Calculate completion percentage (0.0 to 1.0)
    porcentaje = iteracion / total
    
    # Calculate number of completed characters in the bar
    completado = int(longitud * porcentaje)
    
    # Calculate number of remaining characters in the bar
    restante = longitud - completado
    
    # Construct the progress bar string with completed and remaining sections
    barra = '[' + '=' * completado + ' ' * restante + ']'
    
    # Write the progress bar to stdout, using \r to return to line start
    # This allows the bar to update in place without creating new lines
    sys.stdout.write('\r' + barra + f' {porcentaje:.1%}')
    
    # Force flush the output buffer to ensure immediate display
    sys.stdout.flush()
