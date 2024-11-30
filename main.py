# -*- coding: gbk -*-
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox, scrolledtext

"""我这辈子费了"""
def fetch_data():
    url = entry_url.get()
    original_string = url
    prefix = "http://"

    # Auto-complete URL if needed
    if "http://" not in url and "https://" not in url:
        url = f"{prefix}{original_string}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            # Page title
            title = soup.title.string if soup.title else "No title"
            result_text.insert(tk.END, f"Page Title: {title}\n\n")

            # Extract links
            result_text.insert(tk.END, "Links:\n")
            links = soup.find_all("a")
            for link in links:
                href = link.get("href")
                text = link.string
                result_text.insert(tk.END, f"Link: {href} - Text: {text}\n")

            # Extract images
            result_text.insert(tk.END, "\nImage Links:\n")
            images = soup.find_all("img")
            for img in images:
                img_src = img.get("src")
                result_text.insert(tk.END, f"Image Link: {img_src}\n")

            # Extract metadata
            result_text.insert(tk.END, "\nMetadata:\n")
            metas = soup.find_all("meta")
            for meta in metas:
                meta_name = meta.get("name") or meta.get("property")
                meta_content = meta.get("content")
                if meta_name and meta_content:
                    result_text.insert(tk.END, f"{meta_name}: {meta_content}\n")
        else:
            messagebox.showerror(
                "Error", f"Request failed with status code: {response.status_code}"
            )
    except Exception as e:
        messagebox.showerror("Error", f"Request failed: {str(e)}")


# GUI setup
root = tk.Tk()
root.title("Web Scraping Tool")

# URL input
frame_top = tk.Frame(root)
frame_top.pack(pady=10)
tk.Label(frame_top, text="Enter the website URL:").pack(side=tk.LEFT)
entry_url = tk.Entry(frame_top, width=50)
entry_url.pack(side=tk.LEFT, padx=5)

# Scrape button
btn_fetch = tk.Button(frame_top, text="Scrape", command=fetch_data)
btn_fetch.pack(side=tk.LEFT, padx=5)

# Display results
result_text = scrolledtext.ScrolledText(root, width=80, height=30)
result_text.pack(padx=10, pady=10)

# Run main loop
root.mainloop()
