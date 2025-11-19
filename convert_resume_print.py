from playwright.sync_api import sync_playwright
import os

def convert_html_to_pdf(html_file, output_pdf):
    abs_html_path = os.path.abspath(html_file)
    abs_output_path = os.path.abspath(output_pdf)
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        page.goto(f'file:///{abs_html_path}')
        
        page.pdf(
            path=abs_output_path,
            format='A4',
            print_background=True,
            margin={
                'top': '0',
                'right': '0',
                'bottom': '0',
                'left': '0'
            }
        )
        
        browser.close()
        print(f"PDF generated successfully: {output_pdf}")

if __name__ == "__main__":
    convert_html_to_pdf('resume-print.html', 'resume.pdf')

