import re
from typing import Optional, List, Final

# --- Configuration Constants ---
PIN_LENGTH: Final[int] = 4
MODULUS: Final[int] = 10
BLOCK_PATTERN: Final[str] = r'\[(.*?)\]'

# --- Arithmetic Core ---

def _calculate_net_change(operations_str: str) -> int:
    """Calculates net change: (Count of '+') - (Count of '-')."""
    plus_count: int = operations_str.count('+')
    minus_count: int = operations_str.count('-')
    return plus_count - minus_count

def _apply_modular_arithmetic(initial_digit: int, net_change: int) -> int:
    """Applies arithmetic modulo 10: (digit + change) % 10."""
    return (initial_digit + net_change) % MODULUS

# --- Block Handling Logic ---

def _handle_normal_block(content: str) -> Optional[int]:
    """Processes a standard block (e.g., '3+-') to calculate its final digit."""
    if not content:
        return None
        
    try:
        initial_char: str = content[0]
        initial_digit: int = int(initial_char)
        operations: str = content[1:]
        
        net_change: int = _calculate_net_change(operations)
        final_value: int = _apply_modular_arithmetic(initial_digit, net_change)
        
        return final_value
        
    except ValueError:
        # Catches cases where the initial character is not a number
        return None

# --- Main Decoding Function ---

def decode_santa_pin(code: str) -> Optional[str]:
    """
    Deciphers Santa's workshop PIN from the encoded block string.
    
    Args:
        code (str): The encoded string (e.g., '[1++][2-][3+][<]').
        
    Returns:
        Optional[str]: The 4-digit PIN string, or None if the code is invalid.
    """
    
    blocks: List[str] = re.findall(BLOCK_PATTERN, code)
    if not blocks:
        return None

    pin_digits: List[int] = []

    # Iterate through each extracted block content
    for block_content in blocks:

        # --- Handle Special Block: [<] ---
        if block_content == '<':
            # Copy the last digit if the history is not empty
            if pin_digits: 
                pin_digits.append(pin_digits[-1])
            
        # --- Handle Normal Block: [nOP...] ---
        else:
            try:
                # Call specialized function to process the arithmetic
                result_digit: Optional[int] = _handle_normal_block(block_content)
                
                if result_digit is not None:
                    pin_digits.append(result_digit)
            
            except Exception:
                # Catch any unexpected processing errors
                continue 

        # Optimization: Stop processing once the required length is met
        if len(pin_digits) >= PIN_LENGTH:
            break

    # 4. Final Validation and Formatting
    
    if len(pin_digits) < PIN_LENGTH:
        return None
    
    # Convert list of integers to the final 4-digit string
    final_pin: str = "".join(map(str, pin_digits))
    return final_pin[:PIN_LENGTH]