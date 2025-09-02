<!--proyect_tittle-->
# 🧠 Heuristic for the Set Covering Problem

<!--proyect_image1_proyect_markdown/image1.png-->
![Main image](proyect_markdown/image1.png)

---

<!--proyect_subtitle_description-->
## ✨ Project Description

<!--proyect_content_description-->
This project implements a heuristic to solve the **Set Covering** problem, a technique used in combinatorial optimization. The goal is to select a minimal subset of sets that cover all required elements while minimizing the total selection cost.

The algorithm is developed in Python and reads data from an external file (`reader1.txt`), where the costs of each set and the coverage relationships between sets and elements are specified. Based on this information, a binary matrix is built to represent which set covers which element, and an iterative improvement heuristic is applied to select the most efficient sets.

---

<!--proyect_subtitle_objective-->
## 🎯 Project Objective

<!--proyect_content_objective-->
The main purpose is to offer a computational solution that addresses the set covering problem heuristically, without relying on exact methods or linear programming. This is useful in scenarios where a fast and sufficiently good solution is needed, such as logistics planning, resource allocation, or network design.

The project aims to illustrate how a modular solution can be built to read data, structure it into matrices, and apply improvement logic based on incremental coverage and accumulated cost.

---

<!--proyect_subtitle_functionality-->
## 🧩 General Functionality

<!--proyect_content_functionality-->
The program flow is divided into several stages:

- **Library import:** Modules such as `numpy`, `cmath`, `ctypes`, and `multiprocessing.dummy` are used for mathematical and structural operations.
- **Data reading:** The file `reader1.txt` is opened, and the dimensions (rows and columns), set costs, and coverage relationships are extracted.
- **Structure initialization:** Lists are created to store the sets (`sets`) and their respective costs (`costos`), along with control variables for the algorithm.
- **Coverage matrix construction:** Binary values (0 or 1) are assigned to indicate whether a set covers a specific element.
- **Heuristic application:** The improvement value of each set (number of elements it covers) is calculated, the set with the highest improvement is selected, its cost is accumulated, and the covered elements are removed for the next iteration.
- **Completion:** The process continues until all elements are covered. The total cost is displayed and compared to an optimal value manually entered by the user.

---

<!--proyect_subtitle_designUX-->
## 🖥️ Interface and User Experience

<!--proyect_content_designUX-->
The program runs in the console, displaying clear messages about the algorithm’s progress, such as the number of rows and columns, selected sets, and accumulated cost. The final interaction allows the user to enter an optimal value to compare the efficiency of the obtained solution.

Although it does not include a graphical interface, the modular design of the code makes it easy to integrate into visual systems or dashboards if extended functionality is desired.

---

<!--proyect_subtitle_architecture-->
## 🏗️ Technical Architecture

<!--proyect_content_architecture-->
The project structure is organized into functional blocks:

- **File reading:** Data extraction from `reader1.txt`.
- **Data processing:** Conversion of text into numeric structures and matrices.
- **Coverage construction:** Binary assignment in the `sets` matrix.
- **Heuristic algorithm:** Improvement evaluation, set selection, coverage update.
- **Final interaction:** Comparison with optimal value and exit from the loop.

All code is contained in a single script, making it easy to analyze, modify, and adapt to other languages or environments.

---

<!--proyect_subtitle_technologies-->
## 🔧 Technologies Used

<!--proyect_content_technologies-->
**Programming language:**
- Python 3.x

**Libraries:**
- `numpy`  
- `cmath`  
- `ctypes`  
- `string`  
- `multiprocessing.dummy`

**Data input:**
- Plain `.txt` file structured by lines and spaces

---

<!--proyect_subtitle_adminPanel-->
## 📂 Data Structure

<!--proyect_content_adminPanel-->
The input file contains:

- One line with the number of rows (elements) and columns (sets).
- One line with the cost of each set.
- Several lines indicating how many sets cover each element and which ones.

The program transforms this information into:

- A list of costs (`costos`)
- A binary matrix (`sets`) representing coverage
- Control variables to iterate over elements and sets

---

<!--proyect_subtitle_contact-->
## 📬 Contact

<!--proyect_content_contact-->
**Email:**
- vielmassalais023@gmail.com  

**Phone:**
- +52 (81) 3233-1206 

**Social Media:**
- GitHub: [@CesarVielmas](https://github.com/CesarVielmas)  
- LinkedIn: [Cesar Vielmas](https://www.linkedin.com/in/cesar-vielmas-324a9b218/)  

---

<!--proyect_subtitle_footer-->
## Heuristic Set Covering
