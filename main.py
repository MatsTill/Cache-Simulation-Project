import random
import tkinter as tk
from tkinter import messagebox
import time

class CacheMemory:
    def __init__(self):
        self.cache_blocks = 32  # Fixed number of cache blocks
        self.cache_line = 64
        self.cache = [None] * self.cache_blocks
        self.fifo_queue = []

    def read_cache(self, block_address):
        if block_address in self.cache:
            return True
        else:
            return False

    def update_cache(self, block_address):
        if None in self.cache:
            empty_index = self.cache.index(None)
            self.cache[empty_index] = block_address
            self.fifo_queue.append(empty_index)
        else:
            replaced_index = self.fifo_queue.pop(0)
            self.cache[replaced_index] = block_address
            self.fifo_queue.append(replaced_index)

class CacheSimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FA + FIFO Cache Simulation")

        self.memory_blocks_var = tk.StringVar()
        self.memory_blocks_var.set("64")  # Default value

        self.choice_var = tk.IntVar()
        self.choice_var.set(1)

        self.create_widgets()

    def create_widgets(self):
        # Input Frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(side=tk.LEFT, padx=10, pady=10)

        tk.Label(input_frame, text="Number of Memory Blocks:").grid(row=0, column=0, padx=10)
        tk.Entry(input_frame, textvariable=self.memory_blocks_var).grid(row=0, column=1)

        tk.Label(input_frame, text="Select Test Case:").grid(row=1, column=0, padx=10)
        tk.Radiobutton(input_frame, text="Sequential Sequence", variable=self.choice_var, value=1).grid(row=1, column=1, sticky="w")
        tk.Radiobutton(input_frame, text="Random Sequence", variable=self.choice_var, value=2).grid(row=2, column=1, sticky="w")
        tk.Radiobutton(input_frame, text="Mid-Repeat Blocks Sequence", variable=self.choice_var, value=3).grid(row=3, column=1, sticky="w")

        tk.Button(input_frame, text="Start Simulation", command=self.run_simulation).grid(row=4, columnspan=2, pady=10)

        # Cache Memory Display
        self.cache_display_frame = tk.Frame(self.root)
        self.cache_display_frame.pack(side=tk.LEFT, padx=10, pady=10)

        tk.Label(self.cache_display_frame, text="Cache Memory Representation").grid(row=0, columnspan=8, pady=(0, 5))

        self.cache_display_labels = [[tk.Label(self.cache_display_frame, text="", width=4, height=2, relief="solid") for _ in range(8)] for _ in range(4)]
        for i in range(4):
            for j in range(8):
                self.cache_display_labels[i][j].grid(row=i + 1, column=j, padx=2, pady=2)

        # Simulation Results
        self.results_frame = tk.Frame(self.root)
        self.results_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        tk.Label(self.results_frame, text="Text Log").grid(row=0, column=0, pady=(0, 5))
        self.text_log = tk.Text(self.results_frame, height=10, width=50)
        self.text_log.grid(row=1, column=0, pady=(0, 10))


        tk.Label(self.results_frame, text="Simulation Results").grid(row=2, column=0, pady=(0, 5))
        self.simulation_results = tk.Text(self.results_frame, height=15, width=50)
        self.simulation_results.grid(row=3, column=0)

        # Button for step-by-step playback
        self.play_button = tk.Button(self.results_frame, text="Play Step by Step", command=self.play_step_by_step)
        self.play_button.grid(row=4, column=0, pady=10)

    def run_simulation(self):
        try:
            memory_blocks = int(self.memory_blocks_var.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for Memory Blocks.")
            return

        if memory_blocks <= 0:
            messagebox.showerror("Error", "Number of Memory Blocks should be greater than 0.")
            return

        cache = CacheMemory()
        test_sequence = self.generate_test_sequence(memory_blocks)

        memory_access_count = 0
        cache_hit = 0
        cache_miss = 0

        for block_address in test_sequence:
            memory_access_count += 1
            if cache.read_cache(block_address):
                cache_hit += 1
            else:
                cache_miss += 1
                cache.update_cache(block_address)

            # Update GUI with each step
            self.update_gui(cache, memory_access_count, cache_hit, cache_miss)

        # Display final results
        self.display_results(cache, memory_blocks, memory_access_count, cache_hit, cache_miss)

    def play_step_by_step(self):
        try:
            memory_blocks = int(self.memory_blocks_var.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for Memory Blocks.")
            return

        if memory_blocks <= 0:
            messagebox.showerror("Error", "Number of Memory Blocks should be greater than 0.")
            return

        cache = CacheMemory()
        test_sequence = self.generate_test_sequence(memory_blocks)

        memory_access_count = 0
        cache_hit = 0
        cache_miss = 0

        for block_address in test_sequence:
            memory_access_count += 1
            if cache.read_cache(block_address):
                cache_hit += 1
            else:
                cache_miss += 1
                cache.update_cache(block_address)

            # Update GUI with each step
            self.update_gui(cache, memory_access_count, cache_hit, cache_miss)
            self.root.update()  # Update the tkinter window
            time.sleep(0.5)  # Adjust the delay as needed

        # Display final results
        self.display_results(cache, memory_blocks, memory_access_count, cache_hit, cache_miss)

    def update_gui(self, cache, memory_access_count, cache_hit, cache_miss):
        # Update cache display
        for i in range(4):
            for j in range(8):
                index = i * 8 + j
                if index < cache.cache_blocks:
                    self.cache_display_labels[i][j].config(text=str(cache.cache[index]))
                else:
                    self.cache_display_labels[i][j].config(text="")

        # Update text log
        log_text = self.text_log.get("1.0", tk.END).strip()
        log_text += f"\n\nStep {memory_access_count}:"
        log_text += f"\nMemory Access Count: {memory_access_count}"
        log_text += f"\nCache Hit Count: {cache_hit}"
        log_text += f"\nCache Miss Count: {cache_miss}"
        log_text += f"\nCache Memory: {cache.cache}"
        self.text_log.delete("1.0", tk.END)
        self.text_log.insert(tk.END, log_text)
        self.text_log.see(tk.END)  # Scroll to the end


    def display_results(self, cache, memory_blocks, memory_access_count, cache_hit, cache_miss):
        cache_hit_rate = cache_hit / memory_access_count
        cache_miss_rate = cache_miss / memory_access_count
        average_memory_access_time = 1 + cache_miss_rate
        total_memory_access_time = memory_access_count * average_memory_access_time

        result_text = f"\nNumber of Cache Blocks: {cache.cache_blocks}"
        result_text += f"\nCache Line Size: {cache.cache_line} words"
        result_text += "\nRead Policy: Load-Through"
        result_text += f"\nNumber of Memory Blocks: {memory_blocks}"
        result_text += f"\nMemory Access Count: {memory_access_count}"
        result_text += f"\nCache Hit Count: {cache_hit}"
        result_text += f"\nCache Miss Count: {cache_miss}"
        result_text += f"\nCache Hit Rate: {cache_hit_rate:.2%}"
        result_text += f"\nCache Miss Rate: {cache_miss_rate:.2%}"
        result_text += f"\nAverage Memory Access Time: {average_memory_access_time:.2f} cycles"
        result_text += f"\nTotal Memory Access Time: {total_memory_access_time:.2f} cycles"

        # Update simulation results text box
        self.simulation_results.delete("1.0", tk.END)
        self.simulation_results.insert(tk.END, result_text)

    def generate_test_sequence(self, memory_blocks):
        if self.choice_var.get() == 1:
           test_sequence = [i % (2 * memory_blocks) for i in range(4 * memory_blocks)]
           test_sequence = test_sequence + test_sequence
           return test_sequence
        elif self.choice_var.get() == 2:
            temp_random = random.sample(range(4*memory_blocks), 4 *memory_blocks) 
            return random.sample(random.choices(temp_random,weights= None, cum_weights= None,k = memory_blocks * 4), 4 * memory_blocks)
        elif self.choice_var.get() == 3:
            temp_dump = [i % (2 * memory_blocks) for i in range(2 * memory_blocks)]
            temp_dump_2 = [i % (memory_blocks - 1) for i in range(memory_blocks - 1)]

            test_sequence = temp_dump_2 + temp_dump
            test_sequence = test_sequence + test_sequence
            test_sequence = test_sequence + test_sequence
            return test_sequence
            
if __name__ == "__main__":
    root = tk.Tk()
    app = CacheSimulationApp(root)
    root.mainloop()
