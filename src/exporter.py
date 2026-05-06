def export_to_excel(df, file_name="sideboard_plan.xlsx"):
    '''
    fonction qui exporte une table de sideboard dans un fichier excel
    '''
    df.to_excel(file_name, index=False)
    print(f"✅ Fichier généré : {file_name}")