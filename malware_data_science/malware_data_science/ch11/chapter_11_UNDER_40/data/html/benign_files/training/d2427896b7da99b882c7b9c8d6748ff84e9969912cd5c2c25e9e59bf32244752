<html>
<head>
<meta http-dquiv="Content-Type" content="text/html" charset="utf-8">
<script type='text/javascript'>

//다음화면으로 이동
function fncNextPage(cCode, cName){
	with(document.apiForm){
		cropSectionCode.value = cCode;
		cropSectionName.value = cName;
		method="get";
		if(cCode=="6"){	//잡초인 경우
			action = "dgnss2.php";
		}else{			//잡초가 아닌 경우
			action = "dgnss1.php";
		}
		target = "_self";
		submit();
	}
}

</script>
</head>

<body>
<form name="apiForm">
<input type="hidden" name="cropSectionCode"/>
<input type="hidden" name="cropSectionName"/>
<?
	include "XMLparse.php"; //XML UTIL

	$apiKey = "";//apiKey - NCPMS에서 신청 후 승인되면 확인 가능
	
	$serviceCode = "SVC11"; // 사진검색 1의 서비스코드(상세한 내용은 Open API 이용안내 참조)
	

	//XML 받을 URL 생성
	$parameter = "apiKey=" . $apiKey;
	$parameter .= "&serviceCode=" ;
	$parameter .= $serviceCode;
	$url = "http://ncpms.rda.go.kr/npmsAPI/service?" . $parameter; 

	
	//XML Parsing
	$xml = file_get_contents($url);
	$parser = new XMLParser($xml);
	$parser->Parse();
	$doc = $parser->document;

	//기본정보
	$buildTime = $parser->document->buildtime[0]->tagData;//생성시간
	$totalCount = $parser->document->totalcount[0]->tagData;//전체 갯수
	$startPoint = $parser->document->startpoint[0]->tagData;//시작지점
	$displayCount = $parser->document->displaycount[0]->tagData;//출력갯수
	$errorCode = $parser->document->errorcode[0]->tagData;//에러코드(에러발생시에만 생성)
	$errorMsg = $parser->document->errormsg[0]->tagData;//에러메시지(에러발생시에만 생성)

?>

<?	if(!empty($errorCode)){	?>
		농촌진흥청 국가농작물 관리시스템 OpenAPI 호출 시 장애가 발생하였습니다.<br/>잠시후에 다시 이용하십시오.
		<br/>
		<?=$errorMsg?>
<?	}else{?>

		<table  border="0" cellspacing="0" cellpadding="0">
		<?if(count($parser->document->list[0]->item) == 0){?>
			<tr>
				<td width="100%" valign="top" style="padding-top:12px;">조회한 정보가 없습니다.</td>
			</tr> 
		<?}else{

				$cnt = 0;
				foreach($parser->document->list[0]->item as $item){
					
					$cropSectionName = $item->cropsectionname[0]->tagData;//사진명
					$thumbImg = $item->thumbimg[0]->tagData;//이미지 URL
					$cropSectionCode = $item->cropsectioncode[0]->tagData; //사진검색2를 위한 키값
				
		?>


			<?if( ($cnt%4) == 0){ ?><!-- 한줄에 4개씩 -->
				<tr>
			<?}?>

				  <td width="25%" valign="top" style="padding-top:12px;text-align:center;"> 
				  
					<a href="javascript:fncNextPage('<?=$cropSectionCode?>','<?=$cropSectionName?>');">
						<img src="<?=$thumbImg?>" width="100px" height="85px" border="0" alt="" style="border:1px #CCC solid;  padding:10px "   />
					</a>
					<br/>
					<span style="padding-top:5px;letter-spacing: -1px; word-spacing: 0px;">
						<a href="javascript:fncNextPage('<?=$cropSectionCode?>','<?=$cropSectionName?>');" style="text-align:center;"><?=$cropSectionName?></a> 
					</span>			
					
				</td>
			<?if( ($cnt%4) == 3){ ?>
				</tr>
			<?}?>
			<?
					$cnt += 1;				
				}
			}
			?>
			  </table>
<?}?>

</body>
</html>