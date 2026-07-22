from caption_generator import generate_caption

print("================================")
print("     IMAGE CAPTIONING AI")
print("================================")

image_path = input("Enter image path: ")

caption = generate_caption(image_path)

print("\nGenerated Caption:")
print(caption)