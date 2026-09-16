from pathlib import Path


def export_to_excel(df, file_name="sideboard_plan.xlsx"):
    '''
    fonction qui exporte une table de sideboard dans un fichier excel
    '''
    df.to_excel(file_name, index=False)
    print(f"✅ Fichier généré : {file_name}")

    # output_path = Path(file_name)

    # df.to_excel(output_path, index=False)

    # return output_path