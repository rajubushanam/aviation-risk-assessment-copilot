def chunk_text(text, chunk_size=500):
    """Split text into chunks of specified word size."""
    words = text.split()
    return [
        " ".join(words[i:i + chunk_size]) 
        for i in range(0, len(words), chunk_size)
    ]