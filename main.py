import sys
from cli_handler import get_queries, save_report
from engine.validators import router

def main():
    # Ask for input via CLI
    user_input = input("Enter Query, File Path, or Directory: ")
    work_load = get_queries(user_input)
    
    final_results = []
    
    for source, query in work_load:
        result = router(query)
        result['source'] = source
        final_results.append(result)
        
        # Immediate Feedback to CLI
        print(f"[{result['status']}] {source}")
        for err in result['errors']:
            print(f"   ! {err}")

    # Save to file
    report_file = save_report(final_results)
    print(f"\nReport saved to outputs/{report_file}")

if __name__ == "__main__":
    main()
