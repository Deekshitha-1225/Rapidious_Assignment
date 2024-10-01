# Rapidious_Assignment
I completed my rapidious assignment using Flask, integrating a machine learning model with EDA insights. Thank you for the opportunity to enhance my skills!
# Link to the files https://drive.google.com/drive/folders/1pruBpqTmO9gdgHb3J2zEGH8KN_bw5wch?usp=sharing
# you can watch here :(https://youtu.be/BVnn18YSOJU)
# The steps I Have followed
Understand the Data: Explored the dataset to grasp its structure and features.
Remove Duplicates: Eliminated any duplicate entries to ensure data integrity.
Find Missing Values: Identified and handled missing values for accurate analysis.
Remove Outliers: Analyzed and removed outliers to enhance model performance.
Impute Missing Values: Used the mean to fill in missing data for numerical features.
Exploratory Data Analysis (EDA): Applied various EDA techniques to gain insights and visualize relationships in the data.
Model Application: Implemented machine learning models, with Gradient Boosting yielding the best performance.
Flask Application: Built a Flask web application to deploy the model, allowing users to input data and receive predictions.
Predicted Target Values: Used the model to predict ratings based on the input features.

# The Insights I have founf from The data are 
# 1. Rating Statistics:
Mean Rating: The average rating is 3.71, indicating a generally positive response to recipes.
Standard Deviation (SD): A value of 1.33 suggests significant variability in ratings, indicating some recipes are rated much lower or higher than others.
Minimum/Maximum Ratings: The dataset contains recipes rated from 0 to 5, reflecting the diversity in recipe quality or appeal.
# 2. Nutritional Content:
Calories:
Mean: The average caloric value is 6,560.65, which is quite high, suggesting many recipes are energy-dense, possibly due to the inclusion of rich dishes or desserts.
Max: The highest calorie count of 30,111,220 raises concerns about potential outliers or data entry errors.
Protein:
Mean: 93.87g of protein per recipe indicates a focus on protein-rich foods, possibly targeting health-conscious consumers.
Max: The highest value of 236,489g seems like an outlier and may warrant further investigation.
Fat:
Mean: 359.95g of fat on average points to many high-fat recipes in the dataset.
Max: The maximum fat content of 1,722,763g suggests possible data quality issues or very rich dishes.
Sodium:
Mean: 6,502.35mg of sodium highlights the presence of many high-sodium recipes, relevant for those with dietary restrictions.
# 3. Rating Distribution:
The histogram shows a U-shaped pattern, with many recipes rated either very highly (4.375, 5.0) or very low (0.0). This U-shaped distribution is notable, with peaks at both ends of the rating spectrum.
# 4. Correlation Insights:
Calories and Rating Correlation: A very weak correlation (0.01) suggests that calorie content does not significantly affect recipe ratings, indicating that factors such as taste or ease of preparation may be more important to users.
# 5. Ingredient-Specific Insights:
Top Ingredients: The most common ingredients include "bon appétit", "peanut free", "soy free", and "tree nut free", showing that many recipes cater to allergy-conscious consumers or those with dietary restrictions.
Avocado Popularity: Recipes with avocado appear frequently, reflecting its popularity in modern, health-focused cuisine.
Protein-Rich Ingredients: Chicken and bacon are common ingredients, indicating their prevalence in protein-heavy dishes.
# 6. Calorie-Dense Recipes:
Desserts: High-calorie recipes are often desserts, such as "Pear-Cranberry Mincemeat Lattice Pie" and "Deep-Dish Wild Blueberry Pie", emphasizing the indulgent nature of these dishes.
Rich, Savory Dishes: Fat-heavy recipes, particularly those featuring lamb and beef, contribute significantly to the high-calorie values.
# 7. Low-Calorie Recipe Insights:
Low-Calorie Dishes: Recipes with fewer calories often consist of vegetable-based dishes, soups, and salads, catering to health-conscious consumers.
Vegan and Low-Calorie Correlation: Many vegan recipes are also low in calories, highlighting the health benefits of plant-based meals.
# 8. Health-Conscious Cooking Trends:
Low-Fat Recipes: A substantial number of recipes offer low-fat alternatives, catering to calorie-conscious individuals.
Gluten-Free Options: The dataset contains a significant number of gluten-free recipes, reflecting the growing demand for gluten-free diets.
# 9. Dietary Preference Insights:
Vegan Recipes: About 20% of the dataset contains vegan recipes, demonstrating the increasing popularity of plant-based diets.
Sugar-Free Recipes: Recipes labeled as "no sugar added" are notable, catering to those with sugar restrictions or preferences for naturally sweetened dishes.
# 10. Cooking Method Trends:
Baking vs. Frying: Baking is the more common cooking method compared to frying, suggesting a healthier cooking trend.
Grilling Popularity: Grilling is also widely used, particularly for meat-heavy recipes, showing a preference for outdoor cooking methods like BBQ.
# 11. Holiday and Special Occasion Recipes:
Holiday Dishes: Recipes designed for holidays like "Christmas" and "Thanksgiving" tend to be highly rated and calorie-dense, reflecting their festive and indulgent nature.
Summer BBQ Recipes: Tags like "Backyard BBQ" and "Grill/Barbecue" are prevalent in summer recipes, especially for meats and grilled vegetables.
# 12. Regional and Geographical Influence:
Regional Specialties: Recipes associated with states like "California" and cities like "New York" tend to highlight fresh produce or seafood.
Southern Cuisine: Dishes tagged with "Alabama" and "Louisiana" often feature comfort food staples like fried chicken and BBQ.
# 13. Specialized Equipment Use:
Food Processor: Recipes requiring tools like food processors indicate that some dishes involve more advanced cooking techniques or equipment.
Blender-Based Recipes: Recipes like smoothies and sauces that use blenders cater to consumers seeking quick, healthy meal options.
# 14. Low-Sodium and Low-Fat Options:
Dietary-Friendly Recipes: The dataset contains a notable amount of low-sodium and low-fat recipes, aligning with dietary preferences or health-conscious consumers looking for lighter meals.
# 15. Recipe Distribution Skew:
Most recipes are rated above 3.75, showing a general preference for higher-rated dishes. However, there are still many recipes rated poorly (closer to 0.0), indicating a wide range of recipe quality.
# 16. Frequency of Cooking Tags:
Tags like "30 days of groceries" and "advance prep required" appear infrequently, indicating that most recipes are designed for quick or immediate preparation, aligning with modern preferences for convenience.
