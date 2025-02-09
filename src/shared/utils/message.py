def split_message_into_chunks(message: str, max_length: int) -> list[str]:
    chunks = []
    current_chunk = ""

    for word in message.split():
        if len(current_chunk) + len(word) + 1 > max_length:
            chunks.append(current_chunk)
            current_chunk = word
        else:
            current_chunk += (" " if current_chunk else "") + word

    if current_chunk:
        chunks.append(current_chunk)

    return chunks
