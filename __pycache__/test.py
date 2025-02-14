a
    7��g  �                   @   sZ   d dl Z d dlZd dlmZ e�d� d dlmZ e�d� d dlmZ G dd� d�Z	dS )	�    N)�word_tokenizeZ	punkt_tab)�	stopwordsr   )�PorterStemmerc                   @   s4   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� ZdS )�	TextToNumc                 C   s
   || _ d S �N)�text)�selfr   � r	   �[C:\Users\sravani\OneDrive\Desktop\OT-1-sentiment-analysis\OT-1-sentiment-analysis-1\test.py�__init__   s    zTextToNum.__init__c                 C   s>   t �dd| j�}t �dd|�}t �dd|�}|�� }|| _d S )N�,� z[^\w\s]z\s+� )�re�subr   �strip�cleaned)r   r   Zcleaned_textZcleaned_datar	   r	   r
   �cleaner   s
    zTextToNum.cleanerc                 C   s   t | j�| _d S r   )r   r   �tkns�r   r	   r	   r
   �token   s    zTextToNum.tokenc                    s$   t �d�� � fdd�| jD �| _d S )N�englishc                    s   g | ]}|� vr|�qS r	   r	   )�.0�i��stopr	   r
   �
<listcomp>   �    z(TextToNum.removeStop.<locals>.<listcomp>)r   �wordsr   �clr   r	   r   r
   �
removeStop   s    
zTextToNum.removeStopc                    s"   t � � � fdd�| jD �| _| jS )Nc                    s   g | ]}� � |��qS r	   )�stem)r   �word�Zpsr	   r
   r      r   z$TextToNum.stemme.<locals>.<listcomp>)r   r   �str   r	   r#   r
   �stemme   s    zTextToNum.stemmeN)�__name__�
__module__�__qualname__r   r   r   r    r%   r	   r	   r	   r
   r   
   s
   r   )
r   ZnltkZnltk.tokenizer   ZdownloadZnltk.corpusr   Z	nltk.stemr   r   r	   r	   r	   r
   �<module>   s   

