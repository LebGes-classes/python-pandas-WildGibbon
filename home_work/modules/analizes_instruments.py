import pandas as pd
import datetime as dt


def filter_warranty(df: pd.DataFrame) -> pd.DataFrame:
    result_df = df[pd.to_datetime(df["warranty_until"], format="mixed") >= pd.to_datetime(dt.datetime.today())]
    result_df["status"] = result_df["status"].apply(normalize_status)
    result_df = result_df.reset_index()

    return result_df


def sort_by_issues(df: pd.DataFrame) -> pd.DataFrame:
    result_df = df.copy()
    result_df["problems"] = df["issues_reported_12mo"] + df["failure_count_12mo"]
    result_df = result_df.sort_values("problems", ascending=False)
    result_df = result_df[result_df["issues_reported_12mo"] > 0]
    result_df["status"] = result_df["status"].apply(normalize_status)
    result_df = result_df.reset_index()

    return result_df[["clinic_id", "problems"]]


def sort_by_calibration_dates(df: pd.DataFrame) -> pd.DataFrame:
    result_df = df[pd.to_datetime(df["last_calibration_date"], format="mixed") <= pd.to_datetime(dt.datetime.today())]
    result_df["last_calibration_date"] = pd.to_datetime(result_df["last_calibration_date"], format="mixed")
    result_df = result_df.sort_values("last_calibration_date", ascending=False)
    result_df["status"] = result_df["status"].apply(normalize_status)
    result_df = result_df.reset_index()

    return result_df


def normalize_status(status: str) -> str:
    status = status.lower()

    if status == "error":
        return "faulty"
    elif status == "broken":
        return "faulty"

    elif status[:5] == "maint":
        return "maintenance_scheduled"
    elif status == "needs_repair":
        return "service_scheduled"
    elif status == "service_scheduled":
        return "maintenance_scheduled"

    elif status.lower() == "ok":
        return "operational"
    elif status == "op":
        return "operational"
    elif status == "working":
        return "operational"

    elif status == "to_install":
        return "planned_installation"
    elif status == "planned":
        return "planned_installation"
    elif status == "scheduled_install":
        return "planned_installation"

    return status

