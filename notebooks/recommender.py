{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "45c79410-211a-41c8-a051-2352a94f0ce5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter risk appetite (Low / Moderate / High):  low\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    amfi_code                               scheme_name  \\\n",
      "14     120507  ICICI Pru Liquid Fund - Regular - Growth   \n",
      "23     120844      Kotak Liquid Fund - Regular - Growth   \n",
      "30     101208       ABSL Liquid Fund - Regular - Growth   \n",
      "\n",
      "                  fund_house category     plan  return_1yr_pct  \\\n",
      "14       ICICI Prudential MF   Liquid  Regular            8.89   \n",
      "23         Kotak Mahindra MF   Liquid  Regular            4.26   \n",
      "30  Aditya Birla Sun Life MF   Liquid  Regular            6.18   \n",
      "\n",
      "    return_3yr_pct  return_5yr_pct  benchmark_3yr_pct  alpha  beta  \\\n",
      "14            7.68            7.94               5.83   1.85  0.26   \n",
      "23            6.18            8.26               4.66   1.52  0.47   \n",
      "30            5.14            7.95               3.96   1.18  0.43   \n",
      "\n",
      "    sharpe_ratio  sortino_ratio  std_dev_ann_pct  max_drawdown_pct  aum_crore  \\\n",
      "14          7.68          10.37              0.5             -2.62      39116   \n",
      "23          6.18           9.70              0.5             -3.81      27623   \n",
      "30          5.14           8.76              0.5             -3.66      38995   \n",
      "\n",
      "    expense_ratio_pct  morningstar_rating risk_grade  \n",
      "14               0.74                   5        Low  \n",
      "23               0.60                   3        Low  \n",
      "30               0.79                   5        Low  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "performance = pd.read_csv(\n",
    "    r\"C:\\Users\\sarth\\Downloads\\capstone mf analysis project\\data\\processed\\scheme_performance_cleaned.csv\"\n",
    ")\n",
    "\n",
    "risk_appetite = input(\"Enter risk appetite (Low / Moderate / High): \").strip().title()\n",
    "\n",
    "recommendations = (\n",
    "    performance[performance['risk_grade'] == risk_appetite]\n",
    "    .sort_values('sharpe_ratio', ascending=False)\n",
    "    .head(3)\n",
    ")\n",
    "\n",
    "print(recommendations)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f07b973-7204-403b-8613-1df819ecf5c7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45a0cace-abf7-4299-9f03-d541a1e309e3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f6885c7a-fdfa-43a3-8a9c-d49385ed48ee",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "978cca4e-e2e6-4c8a-b95b-71f1121723f0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c786c9d4-420b-4a35-a05e-90248d549129",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "925ee3c6-c42b-4d7a-92d0-999dd580ab84",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3844e1e-4654-4901-bbdb-630f26a2ac07",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1f974810-9515-4388-a0cf-815b1935de45",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78bfbcdb-3fad-4842-921f-5c2961d3726b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
