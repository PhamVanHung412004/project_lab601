import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

class show_plot:
    def __init__(self, h : int, 
                 w : int, 
                 subjects : str,
                 solieu : int,
                 title : str, 
                 x_label: str,
                 y_label : str,
                 check : bool) -> None:
        
        self.h = h
        self.w = w
        self.subjects = subjects
        self.solieu = solieu
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.check = check
    def plot(self):
        fig, ax = plt.subplots(figsize=(self.h, self.w))
        # fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(self.subjects, self.solieu, color='skyblue', edgecolor='black')
        ax.set_title(self.title)
        ax.set_xlabel(self.x_label)
        ax.set_ylabel(self.y_label)
        ax.grid(axis='y', alpha=0.75)
        if (self.check): 
            for bar in bars:
                height = bar.get_height()
                ax.annotate(f'{height}',
                            xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')
                
        st.pyplot(fig)

# Vẽ biểu đồ tròn
class piechart:
    def __init__(self, sizes : list, colors : list, labels : list, title : str) -> None:
        self.sizes = sizes
        self.colors = colors
        self.labels = labels
        self.title = title
    def show(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.pie(self.sizes, labels=self.labels, colors=self.colors, autopct='%1.1f%%',
        pctdistance=1.1, labeldistance=.6,textprops={'size': 'smaller'}, radius=0.5)
        ax.axis('equal') 
        ax.legend(self.labels, loc="center left", bbox_to_anchor=(1, 0.5))
        plt.title(self.title)
        st.pyplot(fig)
