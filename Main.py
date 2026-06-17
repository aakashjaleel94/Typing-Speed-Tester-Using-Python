import time #Measures the time taken to type the sentence 
import random # importing the random module to generate random numbers  

sentences = ["The cat is on the roof.",
            "I love to eat pizza.",
            "The sun is shining brightly.", 
            "She is reading a book.", 
            "The dog is barking loudly."]  #Sample sentences for the typing speed test
def typing_speed_test():
    sentence = random.choice(sentences) # selecting a random sentence from the list 
    print("Type the following sentence: ")
    print(sentence)
    print("Start typing and press Enter when you're done: ") 
    start_time = time.time() # recording the start time 
    user_input = input() # taking user input 
    end_time = time.time() # recording the end time 
    
    time_taken = end_time - start_time # calculating the time taken to type the sentence 
    words_typed = len(user_input.split()) # counting the number of words typed by the user 
    wpm = (words_typed / time_taken) * 60 # calculating words per minute (WPM) 
    if user_input.strip() == sentence: #if sentence is correct then print "Correct!" else print "Incorrect!"
        print("Correct!")
    else:
        print("Incorrect!") 
    print(f"Your typing speed is: {wpm:.2f} WPM") # displaying the typing speed to the user 
typing_speed_test() # calling the function to start the typing speed test
