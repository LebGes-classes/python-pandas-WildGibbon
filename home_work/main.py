import modules.analizes_instruments as inst
import pandas as pd


def main() -> None:
    df: pd.DataFrame = pd.read_excel("data/medical_diagnostic_devices_10000.xlsx")

    with pd.ExcelWriter("data/output.xlsx") as writer:
        inst.sort_by_calibration_dates(df).to_excel(writer, sheet_name='calibration_dates')
        inst.filter_warranty(df).to_excel(writer, sheet_name='warranty')
        inst.sort_by_issues(df).to_excel(writer, sheet_name='issues')


if __name__ == "__main__":
    main()
