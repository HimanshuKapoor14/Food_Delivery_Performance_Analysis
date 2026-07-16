import matplotlib.pyplot as plt
def dataset_info(df):
    print("\nDataset Information:")
    print(df.info())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nStatistical Summary:")
    print(df.describe())


def delivery_time_distribution(df):
    plt.figure(figsize=(8,5))
    plt.hist(df["Time_taken (min)"], bins=20)
    plt.title("Delivery Time Distribution")
    plt.xlabel("Time Taken (Minutes)")
    plt.ylabel("Number of Orders")
    plt.savefig("output/delivery_time_distribution.png")
    plt.show()

def avg_delivery_time_by_city(df):
    plt.figure(figsize=(8,5))
    df.groupby("City")["Time_taken (min)"].mean().plot(kind="bar")
    plt.title("Average Delivery Time by City")
    plt.xlabel("City")
    plt.ylabel("Average Time (Minutes)")
    plt.savefig("output/avg_delivery_time_by_city.png")
    plt.show()

def avg_delivery_time_by_weather(df):
    plt.figure(figsize=(8,5))
    df.groupby("Weather_conditions")["Time_taken (min)"].mean().plot(kind="bar")
    plt.title("Average Delivery Time by Weather")
    plt.xlabel("Weather")
    plt.ylabel("Average Time (Minutes)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("output/avg_delivery_time_by_weather.png")
    plt.show()

def avg_delivery_time_by_traffic(df):
    plt.figure(figsize=(8,5))
    df.groupby("Road_traffic_density")["Time_taken (min)"].mean().plot(kind="bar")
    plt.title("Average Delivery Time by Traffic")
    plt.xlabel("Traffic Density")
    plt.ylabel("Average Time (Minutes)")
    plt.tight_layout()
    plt.savefig("output/avg_delivery_time_by_traffic.png")
    plt.show()

def avg_delivery_time_by_vehicle(df):
    plt.figure(figsize=(8,5))
    df.groupby("Type_of_vehicle")["Time_taken (min)"].mean().plot(kind="bar")
    plt.title("Average Delivery Time by Vehicle Type")
    plt.xlabel("Vehicle Type")
    plt.ylabel("Average Time (Minutes)")
    plt.tight_layout()
    plt.savefig("output/avg_delivery_time_by_vehicle.png")
    plt.show()

def delivery_count_by_city(df):
    plt.figure(figsize=(8,5))
    df["City"].value_counts().plot(kind="bar")
    plt.title("Delivery Count by City")
    plt.xlabel("City")
    plt.ylabel("Number of Deliveries")
    plt.tight_layout()
    plt.savefig("output/delivery_count_by_city.png")
    plt.show()

def ratings_distribution(df):
    plt.figure(figsize=(8,5))
    plt.hist(df["Delivery_person_Ratings"], bins=15)
    plt.title("Delivery Person Ratings Distribution")
    plt.xlabel("Ratings")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("output/ratings_distribution.png")
    plt.show()