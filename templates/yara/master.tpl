/*
Example Yara Rule. Use this as a template for creating your own Yara rules! 
Please modify template for your use case! Have phun! 
*/
rule example_rule
{
	meta:
		created   = ""
		modified  = ""
		author    = ""
		version   = "" 
		vendor    = ""
		reference = ""
	strings:
		$textstring1 = "" ascii wide nocase
		$textstring2 = "" ascii wide nocase
		$textstring3 = "" ascii wide nocase
	condition:
		$textstring1 and $textstring2 and $textstring3
}