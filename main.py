from pathlib import Path

from parser import EmlParser


def main():
    parser = EmlParser()

    for eml_path in Path("emails").glob("**/*.eml"):
        mail = parser.parse(eml_path)

        print(f"\n{'='*60}")
        print(f"File   : {mail.source_path}")
        print(f"Subject: {mail.metadata.subject}")
        print(f"From   : {mail.metadata.mail_from}")
        print(f"To     : {', '.join(mail.metadata.mail_to)}")
        print(f"Date   : {mail.metadata.date}")
        print(f"Attachments: {len(mail.attachments)}")

        for att in mail.attachments:
            parser.enrich(att)
            print(f"\n  [{att.extension}] {att.filename}")
            if att.info is None:
                print("    (no info extracted)")
            elif att.is_excel():
                info = att.info
                for sheet in info.sheets:
                    print(f"    Sheet '{sheet}': {info.row_count[sheet]} rows, {info.col_count[sheet]} cols")
                    print(f"    Headers: {info.headers[sheet]}")
            elif att.is_pdf():
                info = att.info
                print(f"    Pages: {info.page_count}")
                if info.text_preview:
                    print(f"    Preview: {info.text_preview[:100]}...")


if __name__ == "__main__":
    main()
