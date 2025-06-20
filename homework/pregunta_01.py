import matplotlib.pyplot as plt
import pandas as pd
import os
import glob

# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """


    def loadData():
        df = pd.read_csv("files/input/shipping-data.csv")
        return df

    def createVisualForShippingPerWarehouse(df):
        df = df.copy()
        plt.figure()

        counts = df.Warehouse_block.value_counts()
        counts.plot.bar(
            title="Shipping per Warehouse Block",
            xlabel="Warehouse Block",
            ylabel="Record Count",
            color="tab:blue",
            fontsize=8,
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.savefig("docs/shipping_per_warehouse.png")

    def createVisualForModeOfShipment(df):
        df = df.copy()
        plt.figure()

        counts = df.Mode_of_Shipment.value_counts()
        counts.plot.pie(
            title="Mode of Shipment",
            wedgeprops=dict(width=0.35),
            ylabel="",
            color=["tab:blue", "tab:orange", "tab:green"],
        )
        plt.savefig("docs/mode_of_shipment.png")

    def createVisualForAverageCustomerRating(df):
        df = df.copy()
        plt.figure()

        df = (
            df[["Mode_of_Shipment", "Customer_rating"]]
            .groupby("Mode_of_Shipment")
            .describe()
        )
        df.columns = df.columns.droplevel()
        df = df[["mean", "min", "max"]]
        plt.barh(
            y=df.index.values,
            width=df["max"].values - 1,
            left=df["min"].values,
            height=0.9,
            color="lightgrey",
            alpha=0.5,
        )

        colors = [
            "tab:green" if value >= 3.0 else "tab:orange" for value in df["mean"].values
        ]

        plt.barh(
            y=df.index.values,
            width=df["mean"].values - 1,
            left=df["min"].values,
            color=colors,
            height=0.5,
            alpha=1.0,
        )

        plt.title("Average Customer Rating by Mode of Shipment")
        plt.gca().spines["left"].set_color("grey")
        plt.gca().spines["bottom"].set_color("grey")
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)

        plt.savefig("docs/average_customer_rating.png")

    def creataVisualForWeightDistribution(df):
        df = df.copy()
        plt.figure()

        df.Weight_in_gms.plot.hist(
            title="Shipped Weight Distribution",
            color="tab:orange",
            edgecolor="white",
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.savefig("docs/weight_distribution.png")

    def createOutputDirectory(outputPath):
        if not os.path.exists(outputPath):
            os.makedirs(outputPath)

    df = loadData()
    createOutputDirectory("docs")
    createVisualForShippingPerWarehouse(df)
    createVisualForModeOfShipment(df)
    createVisualForAverageCustomerRating(df)
    creataVisualForWeightDistribution(df)